namespace Lab_1
{
    partial class midTextBox
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.dataGridViewParent = new System.Windows.Forms.DataGridView();
            this.dataGridViewChild = new System.Windows.Forms.DataGridView();
            this.echipeTextBox = new System.Windows.Forms.TextBox();
            this.label1 = new System.Windows.Forms.Label();
            this.scorTextBox = new System.Windows.Forms.TextBox();
            this.label2 = new System.Windows.Forms.Label();
            this.nrSpectatoriTextBox = new System.Windows.Forms.TextBox();
            this.label3 = new System.Windows.Forms.Label();
            this.idCompetitieTextBox = new System.Windows.Forms.TextBox();
            this.adaugareButton = new System.Windows.Forms.Button();
            this.stergereButton = new System.Windows.Forms.Button();
            this.actualizareButton = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.messageToUser = new System.Windows.Forms.Label();
            this.label5 = new System.Windows.Forms.Label();
            this.idMeciTextBox = new System.Windows.Forms.TextBox();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).BeginInit();
            this.SuspendLayout();
            // 
            // dataGridViewParent
            // 
            this.dataGridViewParent.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewParent.Location = new System.Drawing.Point(12, 12);
            this.dataGridViewParent.Name = "dataGridViewParent";
            this.dataGridViewParent.Size = new System.Drawing.Size(261, 223);
            this.dataGridViewParent.TabIndex = 0;
            this.dataGridViewParent.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView_Competitie_CellContentClick);
            // 
            // dataGridViewChild
            // 
            this.dataGridViewChild.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.dataGridViewChild.Location = new System.Drawing.Point(292, 12);
            this.dataGridViewChild.Name = "dataGridViewChild";
            this.dataGridViewChild.Size = new System.Drawing.Size(426, 223);
            this.dataGridViewChild.TabIndex = 1;
            this.dataGridViewChild.CellContentClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.dataGridView_Meci_CellContentClick);
            // 
            // echipeTextBox
            // 
            this.echipeTextBox.Location = new System.Drawing.Point(73, 315);
            this.echipeTextBox.Name = "echipeTextBox";
            this.echipeTextBox.Size = new System.Drawing.Size(200, 20);
            this.echipeTextBox.TabIndex = 2;
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(12, 318);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(40, 13);
            this.label1.TabIndex = 3;
            this.label1.Text = "Echipe";
            this.label1.Click += new System.EventHandler(this.label1_Click);
            // 
            // scorTextBox
            // 
            this.scorTextBox.Location = new System.Drawing.Point(73, 349);
            this.scorTextBox.Name = "scorTextBox";
            this.scorTextBox.Size = new System.Drawing.Size(200, 20);
            this.scorTextBox.TabIndex = 4;
            this.scorTextBox.TextChanged += new System.EventHandler(this.scorTextBox_TextChanged);
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Location = new System.Drawing.Point(20, 352);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(29, 13);
            this.label2.TabIndex = 5;
            this.label2.Text = "Scor";
            this.label2.Click += new System.EventHandler(this.label2_Click);
            // 
            // nrSpectatoriTextBox
            // 
            this.nrSpectatoriTextBox.Location = new System.Drawing.Point(73, 384);
            this.nrSpectatoriTextBox.Name = "nrSpectatoriTextBox";
            this.nrSpectatoriTextBox.Size = new System.Drawing.Size(200, 20);
            this.nrSpectatoriTextBox.TabIndex = 6;
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Location = new System.Drawing.Point(1, 387);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(66, 13);
            this.label3.TabIndex = 7;
            this.label3.Text = "NrSpectatori";
            // 
            // idCompetitieTextBox
            // 
            this.idCompetitieTextBox.Location = new System.Drawing.Point(73, 418);
            this.idCompetitieTextBox.Name = "idCompetitieTextBox";
            this.idCompetitieTextBox.Size = new System.Drawing.Size(200, 20);
            this.idCompetitieTextBox.TabIndex = 8;
            // 
            // adaugareButton
            // 
            this.adaugareButton.Location = new System.Drawing.Point(338, 274);
            this.adaugareButton.Name = "adaugareButton";
            this.adaugareButton.Size = new System.Drawing.Size(75, 23);
            this.adaugareButton.TabIndex = 10;
            this.adaugareButton.Text = "Adaugare";
            this.adaugareButton.UseVisualStyleBackColor = true;
            this.adaugareButton.Click += new System.EventHandler(this.adaugareButton_Click);
            // 
            // stergereButton
            // 
            this.stergereButton.Location = new System.Drawing.Point(338, 312);
            this.stergereButton.Name = "stergereButton";
            this.stergereButton.Size = new System.Drawing.Size(75, 23);
            this.stergereButton.TabIndex = 11;
            this.stergereButton.Text = "Stergere";
            this.stergereButton.UseVisualStyleBackColor = true;
            this.stergereButton.Click += new System.EventHandler(this.stergereButton_Click);
            // 
            // actualizareButton
            // 
            this.actualizareButton.Location = new System.Drawing.Point(338, 349);
            this.actualizareButton.Name = "actualizareButton";
            this.actualizareButton.Size = new System.Drawing.Size(75, 23);
            this.actualizareButton.TabIndex = 12;
            this.actualizareButton.Text = "Actualizare";
            this.actualizareButton.UseVisualStyleBackColor = true;
            this.actualizareButton.Click += new System.EventHandler(this.actualizareButton_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Location = new System.Drawing.Point(27, 421);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(22, 13);
            this.label4.TabIndex = 13;
            this.label4.Text = "Cid";
            // 
            // messageToUser
            // 
            this.messageToUser.AutoSize = true;
            this.messageToUser.Location = new System.Drawing.Point(12, 240);
            this.messageToUser.Name = "messageToUser";
            this.messageToUser.Size = new System.Drawing.Size(35, 13);
            this.messageToUser.TabIndex = 14;
            this.messageToUser.Text = "label5";
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Location = new System.Drawing.Point(23, 283);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(24, 13);
            this.label5.TabIndex = 15;
            this.label5.Text = "Mid";
            this.label5.Click += new System.EventHandler(this.label5_Click);
            // 
            // idMeciTextBox
            // 
            this.idMeciTextBox.Location = new System.Drawing.Point(73, 280);
            this.idMeciTextBox.Name = "idMeciTextBox";
            this.idMeciTextBox.Size = new System.Drawing.Size(200, 20);
            this.idMeciTextBox.TabIndex = 16;
            // 
            // midTextBox
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.idMeciTextBox);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.actualizareButton);
            this.Controls.Add(this.stergereButton);
            this.Controls.Add(this.adaugareButton);
            this.Controls.Add(this.idCompetitieTextBox);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.nrSpectatoriTextBox);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.scorTextBox);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.echipeTextBox);
            this.Controls.Add(this.dataGridViewChild);
            this.Controls.Add(this.dataGridViewParent);
            this.Controls.Add(this.messageToUser);
            this.Name = "midTextBox";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewParent)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.dataGridViewChild)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.DataGridView dataGridViewParent;

        private System.Windows.Forms.DataGridView dataGridViewChild;

        private System.Windows.Forms.Label messageToUser;

        private System.Windows.Forms.TextBox denumireTextBox;

        private System.Windows.Forms.TextBox competitieIdTextBox;

       

        private System.Windows.Forms.TextBox echipeTextBox;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.TextBox scorTextBox;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.TextBox nrSpectatoriTextBox;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.TextBox idCompetitieTextBox;
        private System.Windows.Forms.Button adaugareButton;
        private System.Windows.Forms.Button stergereButton;
        private System.Windows.Forms.Button actualizareButton;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.TextBox idMeciTextBox;
    }
}

