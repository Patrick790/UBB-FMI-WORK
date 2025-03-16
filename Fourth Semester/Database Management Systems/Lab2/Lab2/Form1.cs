using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;
using System.Data.SqlClient;
using System.Windows.Markup;
using System.Net.NetworkInformation;
using System.Configuration;
using System.Windows.Forms.VisualStyles;

namespace Lab_1
{
    public partial class Form1 : Form
    { 

        static string connectionString = ConfigurationManager.ConnectionStrings["connection"].ConnectionString;
        SqlConnection connection = new SqlConnection(connectionString);
        SqlDataAdapter dataAdapterParent = new SqlDataAdapter();

        DataSet dataSetParent = new DataSet();

        SqlDataAdapter dataAdapterChild = new SqlDataAdapter();

        private DataSet dataSetChild = new DataSet();


        public Form1()
        {
            InitializeComponent();
        }
    

        private void Form1_Load(object sender, EventArgs e)
        {
            try
            {
                string selectQuery = ConfigurationManager.AppSettings["ParentSelect"];
                dataAdapterParent.SelectCommand = new SqlCommand(selectQuery, connection);
                dataSetParent.Clear();
                dataAdapterParent.Fill(dataSetParent);
                dataGridViewParent.DataSource = dataSetParent.Tables[0];
                generateTextBoxes_Parent();
                generateTextBoxes_Child();
                tableName_Parent.Text = ConfigurationManager.AppSettings["ParentTableName"];
                tableName_Child.Text = ConfigurationManager.AppSettings["ChildTableName"];



            }
            catch (Exception ex)
            {
                messageToUser.Text += ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
                connection.Close();
            }

           

        }

        private void generateTextBoxes_Parent()
        {
            List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ParentColumnNames"].Split(','));
            int pointX = 10;
            int pointY = 10;
            panel_Parent.Controls.Clear();
            foreach (string columnName in columnNames)
            {
                Label label = new Label
                {
                    Text = columnName,
                    Name = columnName + "Label",
                    Location = new Point(pointX, pointY),
                    Visible = true,
                    Parent = panel_Parent
                };

                TextBox textBox = new TextBox
                {
                    Name = columnName,
                    Location = new Point(pointX + label.Width, pointY),
                    Visible = true,
                    Enabled = false,
                    Parent = panel_Parent
                };
                
                pointY += 30;
                panel_Parent.Show();
            }
            
        }

        private void generateTextBoxes_Child()
        {
            List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
            string parentID = ConfigurationManager.AppSettings["parentID"];
            string childID = ConfigurationManager.AppSettings["childID"];

            int pointX = 10;
            int pointY = 10;
            panel_Child.Controls.Clear();

            foreach (string columnName in columnNames)
            {
                Label label = new Label
                {
                    Text = columnName,
                    Name = columnName + "Label",
                    Location = new Point(pointX, pointY),
                    Visible = true,
                    Parent = panel_Child
                };

                TextBox textBox = new TextBox
                {
                    Name = columnName,
                    Location = new Point(pointX + label.Width, pointY),
                    Visible = true,
                    Parent = panel_Child,
                };

                if (columnName == childID)
                {
                    textBox.Enabled = false;
                }

                pointY += 30;
                panel_Child.Show();
            }
        }

        private void dataGrid_Parent_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
                messageToUser.Text = "";
                
                List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ParentColumnNames"].Split(','));
                int i = 0;
                int id = -1;
                string parentID = ConfigurationManager.AppSettings["parentID"];
                foreach (string columnName in columnNames)
                {
                    TextBox textBox = (TextBox)panel_Parent.Controls[columnName];
                    textBox.Text = dataGridViewParent.CurrentRow.Cells[i].FormattedValue.ToString();
                    if (columnName == parentID)
                    {
                        id = int.Parse(textBox.Text);
                    }

                    i++;
                }

                try
                {
                    string SelectQuery = ConfigurationManager.AppSettings["ChildSelect"];

                    dataAdapterChild.SelectCommand = new SqlCommand(SelectQuery, connection);
                    dataAdapterChild.SelectCommand.Parameters.AddWithValue("@" + parentID, id);

                    dataSetChild.Clear();
                    dataAdapterChild.Fill(dataSetChild);
                    dataGridViewChild.DataSource = dataSetChild.Tables[0];
                }
                catch (Exception ex)
                {
                    messageToUser.Text += ex.Message;
                    messageToUser.ForeColor = Color.DarkRed;
                    connection.Close();
                }
        }
        
        
        private void dataGrid_Child_RowHeaderMouseClick(object sender, DataGridViewCellMouseEventArgs e)
        {
            List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
            int i = 0;
            foreach (string columnName in columnNames)
            {
                TextBox textBox = (TextBox)panel_Child.Controls[columnName];
                textBox.Text = dataGridViewChild.CurrentRow.Cells[i].FormattedValue.ToString();
                i++;
            }
        }

        private void addButton_Click(object sender, EventArgs e)
        {
            messageToUser.Text = "";
            try
            {
                string InsertQuery = ConfigurationManager.AppSettings["InsertQuery"];
                List<string> commandParameters =
                    new List<string>(ConfigurationManager.AppSettings["InsertCommandParameters"].Split(','));
                List<string> columnNames =
                    new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

                dataAdapterChild.InsertCommand = new SqlCommand(InsertQuery, connection);
                foreach (string columnName in columnNames)
                {
                    if (commandParameters.Where(x => x.Contains(columnName)).FirstOrDefault() != null)
                    {
                        TextBox textBox = (TextBox)panel_Child.Controls[columnName];
                        if (textBox.Text == "")
                        {
                            throw new Exception("Campurile nu pot fi goale!");
                        }

                        dataAdapterChild.InsertCommand.Parameters.AddWithValue("@" + columnName, textBox.Text);
                    }
                }

                connection.Open();
                dataAdapterChild.InsertCommand.ExecuteNonQuery();
                connection.Close();

                messageToUser.Text = "Adaugare efectuata cu succes!";
                messageToUser.ForeColor = Color.DarkGreen;

                dataSetChild.Clear();
                dataAdapterChild.Fill(dataSetChild);
                dataGridViewChild.DataSource = dataSetChild.Tables[0];
            }
            catch (Exception ex)
            {
                messageToUser.Text += ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
                connection.Close();
            }
        }


        private void deleteButton_Click(object sender, EventArgs e)
        {
            messageToUser.Text = "";
            
            List<string> columnNames = new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));
            int i = 0;
            int id = -1;
            string childID = ConfigurationManager.AppSettings["ChildID"];
            foreach (string columnName in columnNames)
            {
                if (columnName == childID)
                {
                    id = int.Parse(dataGridViewChild.CurrentRow.Cells[i].FormattedValue.ToString());
                }

                i++;
            }

            try
            {
                string DeleteQuery = ConfigurationManager.AppSettings["DeleteQuery"];

                dataAdapterChild.DeleteCommand = new SqlCommand(DeleteQuery, connection);
                dataAdapterChild.DeleteCommand.Parameters.AddWithValue("@" + childID, id);

                connection.Open();
                dataAdapterChild.DeleteCommand.ExecuteNonQuery();
                connection.Close();

                messageToUser.Text = "Stergere efectuata cu succes!";
                messageToUser.ForeColor = Color.DarkGreen;

                dataSetChild.Clear();
                dataAdapterChild.Fill(dataSetChild);
                dataGridViewChild.DataSource = dataSetChild.Tables[0];
            }
            catch (Exception ex)
            {
                messageToUser.Text += ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
                connection.Close();
            }
        }

        private void updateButton_Click(object sender, EventArgs e)
        {
            messageToUser.Text = "";
            try
            {
                string UpdateQuery = ConfigurationManager.AppSettings["UpdateQuery"];
                List<string> commandParameters =
                    new List<string>(ConfigurationManager.AppSettings["UpdateCommandParameters"].Split(','));
                List<string> columnNames =
                    new List<string>(ConfigurationManager.AppSettings["ChildColumnNames"].Split(','));

                dataAdapterChild.UpdateCommand = new SqlCommand(UpdateQuery, connection);
                foreach (string columnName in columnNames)
                {
                    if (commandParameters.Where(x => x.Contains(columnName)).FirstOrDefault() != null)
                    {
                        TextBox textBox = (TextBox)panel_Child.Controls[columnName];
                        if (textBox.Text == "")
                        {
                            throw new Exception("Campurile nu pot fi goale!");
                        }
                        if (columnName == "Inaltime" || columnName == "Varsta" || columnName == "NrSpectatori")
                        {
                            if (!int.TryParse(textBox.Text, out _))
                            {
                                throw new Exception("Valoarea introdusă pentru " + columnName + " nu este un număr valid.");
                            }
                        }

                        dataAdapterChild.UpdateCommand.Parameters.AddWithValue("@" + columnName, textBox.Text);
                    }
                }

                connection.Open();
                dataAdapterChild.UpdateCommand.ExecuteNonQuery();
                connection.Close();

                messageToUser.Text = "Actualizare efectuata cu succes!";
                messageToUser.ForeColor = Color.DarkGreen;

                dataSetChild.Clear();
                dataAdapterChild.Fill(dataSetChild);
                dataGridViewChild.DataSource = dataSetChild.Tables[0];
            }
            catch (Exception ex)
            {
                messageToUser.Text += ex.Message;
                messageToUser.ForeColor = Color.DarkRed;
                connection.Close();
            }
        }
        
        


    }
}




