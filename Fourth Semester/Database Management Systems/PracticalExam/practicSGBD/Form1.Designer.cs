namespace practicSGBD
{
    partial class Form1
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
            this.tipFructeComboBox = new System.Windows.Forms.ComboBox();
            this.fructeGridView = new System.Windows.Forms.DataGridView();
            this.FidLabel = new System.Windows.Forms.Label();
            this.fidTextBox = new System.Windows.Forms.TextBox();
            this.denumireLabel = new System.Windows.Forms.Label();
            this.denumireTextBox = new System.Windows.Forms.TextBox();
            this.culoareLabel = new System.Windows.Forms.Label();
            this.culoareTextBox = new System.Windows.Forms.TextBox();
            this.lunaOptimaLabel = new System.Windows.Forms.Label();
            this.lunaOptimaTextBox = new System.Windows.Forms.TextBox();
            this.pretMediuLabel = new System.Windows.Forms.Label();
            this.pretMediuTextBox = new System.Windows.Forms.TextBox();
            this.tidLabel = new System.Windows.Forms.Label();
            this.tidTextBox = new System.Windows.Forms.TextBox();
            this.adaugaButton = new System.Windows.Forms.Button();
            this.stergeButton = new System.Windows.Forms.Button();
            this.modificaButton = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.fructeGridView)).BeginInit();
            this.SuspendLayout();
            // 
            // tipFructeComboBox
            // 
            this.tipFructeComboBox.FormattingEnabled = true;
            this.tipFructeComboBox.Location = new System.Drawing.Point(161, 77);
            this.tipFructeComboBox.Name = "tipFructeComboBox";
            this.tipFructeComboBox.Size = new System.Drawing.Size(160, 28);
            this.tipFructeComboBox.TabIndex = 0;
            this.tipFructeComboBox.SelectedIndexChanged += new System.EventHandler(this.tipFructeComboBox_SelectedIndexChanged);
            // 
            // fructeGridView
            // 
            this.fructeGridView.ColumnHeadersHeightSizeMode = System.Windows.Forms.DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            this.fructeGridView.Location = new System.Drawing.Point(403, 77);
            this.fructeGridView.Name = "fructeGridView";
            this.fructeGridView.RowTemplate.Height = 28;
            this.fructeGridView.Size = new System.Drawing.Size(305, 226);
            this.fructeGridView.TabIndex = 1;
            this.fructeGridView.CellClick += new System.Windows.Forms.DataGridViewCellEventHandler(this.gridViewFructe_CellClick);
            // 
            // FidLabel
            // 
            this.FidLabel.Location = new System.Drawing.Point(12, 225);
            this.FidLabel.Name = "FidLabel";
            this.FidLabel.Size = new System.Drawing.Size(38, 23);
            this.FidLabel.TabIndex = 2;
            this.FidLabel.Text = "Fid";
            // 
            // fidTextBox
            // 
            this.fidTextBox.Location = new System.Drawing.Point(57, 222);
            this.fidTextBox.Name = "fidTextBox";
            this.fidTextBox.Size = new System.Drawing.Size(100, 26);
            this.fidTextBox.TabIndex = 3;
            // 
            // denumireLabel
            // 
            this.denumireLabel.Location = new System.Drawing.Point(12, 260);
            this.denumireLabel.Name = "denumireLabel";
            this.denumireLabel.Size = new System.Drawing.Size(79, 23);
            this.denumireLabel.TabIndex = 4;
            this.denumireLabel.Text = "Denumire";
            // 
            // denumireTextBox
            // 
            this.denumireTextBox.Location = new System.Drawing.Point(97, 257);
            this.denumireTextBox.Name = "denumireTextBox";
            this.denumireTextBox.Size = new System.Drawing.Size(120, 26);
            this.denumireTextBox.TabIndex = 5;
            // 
            // culoareLabel
            // 
            this.culoareLabel.Location = new System.Drawing.Point(12, 300);
            this.culoareLabel.Name = "culoareLabel";
            this.culoareLabel.Size = new System.Drawing.Size(68, 23);
            this.culoareLabel.TabIndex = 6;
            this.culoareLabel.Text = "Culoare";
            // 
            // culoareTextBox
            // 
            this.culoareTextBox.Location = new System.Drawing.Point(86, 300);
            this.culoareTextBox.Name = "culoareTextBox";
            this.culoareTextBox.Size = new System.Drawing.Size(118, 26);
            this.culoareTextBox.TabIndex = 7;
            // 
            // lunaOptimaLabel
            // 
            this.lunaOptimaLabel.Location = new System.Drawing.Point(12, 338);
            this.lunaOptimaLabel.Name = "lunaOptimaLabel";
            this.lunaOptimaLabel.Size = new System.Drawing.Size(100, 23);
            this.lunaOptimaLabel.TabIndex = 8;
            this.lunaOptimaLabel.Text = "Luna optima";
            // 
            // lunaOptimaTextBox
            // 
            this.lunaOptimaTextBox.Location = new System.Drawing.Point(118, 335);
            this.lunaOptimaTextBox.Name = "lunaOptimaTextBox";
            this.lunaOptimaTextBox.Size = new System.Drawing.Size(100, 26);
            this.lunaOptimaTextBox.TabIndex = 9;
            // 
            // pretMediuLabel
            // 
            this.pretMediuLabel.Location = new System.Drawing.Point(12, 375);
            this.pretMediuLabel.Name = "pretMediuLabel";
            this.pretMediuLabel.Size = new System.Drawing.Size(85, 23);
            this.pretMediuLabel.TabIndex = 10;
            this.pretMediuLabel.Text = "Pret mediu";
            // 
            // pretMediuTextBox
            // 
            this.pretMediuTextBox.Location = new System.Drawing.Point(104, 372);
            this.pretMediuTextBox.Name = "pretMediuTextBox";
            this.pretMediuTextBox.Size = new System.Drawing.Size(100, 26);
            this.pretMediuTextBox.TabIndex = 11;
            // 
            // tidLabel
            // 
            this.tidLabel.Location = new System.Drawing.Point(12, 407);
            this.tidLabel.Name = "tidLabel";
            this.tidLabel.Size = new System.Drawing.Size(50, 23);
            this.tidLabel.TabIndex = 12;
            this.tidLabel.Text = "Tid";
            // 
            // tidTextBox
            // 
            this.tidTextBox.Location = new System.Drawing.Point(57, 407);
            this.tidTextBox.Name = "tidTextBox";
            this.tidTextBox.Size = new System.Drawing.Size(100, 26);
            this.tidTextBox.TabIndex = 13;
            // 
            // adaugaButton
            // 
            this.adaugaButton.Location = new System.Drawing.Point(300, 319);
            this.adaugaButton.Name = "adaugaButton";
            this.adaugaButton.Size = new System.Drawing.Size(102, 34);
            this.adaugaButton.TabIndex = 14;
            this.adaugaButton.Text = "adauga";
            this.adaugaButton.UseVisualStyleBackColor = true;
            this.adaugaButton.Click += new System.EventHandler(this.adaugaButton_Click);
            // 
            // stergeButton
            // 
            this.stergeButton.Location = new System.Drawing.Point(300, 359);
            this.stergeButton.Name = "stergeButton";
            this.stergeButton.Size = new System.Drawing.Size(102, 29);
            this.stergeButton.TabIndex = 15;
            this.stergeButton.Text = "sterge";
            this.stergeButton.UseVisualStyleBackColor = true;
            this.stergeButton.Click += new System.EventHandler(this.buttonSterge_Click);
            // 
            // modificaButton
            // 
            this.modificaButton.Location = new System.Drawing.Point(300, 394);
            this.modificaButton.Name = "modificaButton";
            this.modificaButton.Size = new System.Drawing.Size(102, 36);
            this.modificaButton.TabIndex = 16;
            this.modificaButton.Text = "modifica";
            this.modificaButton.UseVisualStyleBackColor = true;
            this.modificaButton.Click += new System.EventHandler(this.buttonModifica_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(9F, 20F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(800, 450);
            this.Controls.Add(this.modificaButton);
            this.Controls.Add(this.stergeButton);
            this.Controls.Add(this.adaugaButton);
            this.Controls.Add(this.tidTextBox);
            this.Controls.Add(this.tidLabel);
            this.Controls.Add(this.pretMediuTextBox);
            this.Controls.Add(this.pretMediuLabel);
            this.Controls.Add(this.lunaOptimaTextBox);
            this.Controls.Add(this.lunaOptimaLabel);
            this.Controls.Add(this.culoareTextBox);
            this.Controls.Add(this.culoareLabel);
            this.Controls.Add(this.denumireTextBox);
            this.Controls.Add(this.denumireLabel);
            this.Controls.Add(this.fidTextBox);
            this.Controls.Add(this.FidLabel);
            this.Controls.Add(this.fructeGridView);
            this.Controls.Add(this.tipFructeComboBox);
            this.Name = "Form1";
            this.Text = "Form1";
            ((System.ComponentModel.ISupportInitialize)(this.fructeGridView)).EndInit();
            this.ResumeLayout(false);
            this.PerformLayout();
        }

        private System.Windows.Forms.TextBox pretMediuTextBox;
        private System.Windows.Forms.Label tidLabel;
        private System.Windows.Forms.Button adaugaButton;
        private System.Windows.Forms.Button stergeButton;
        private System.Windows.Forms.Button modificaButton;

        private System.Windows.Forms.TextBox tidTextBox;

        private System.Windows.Forms.Label pretMediuLabel;

        private System.Windows.Forms.TextBox lunaOptimaTextBox;

        private System.Windows.Forms.Label culoareLabel;
        private System.Windows.Forms.TextBox culoareTextBox;
        private System.Windows.Forms.Label lunaOptimaLabel;

        private System.Windows.Forms.Label denumireLabel;
        private System.Windows.Forms.TextBox denumireTextBox;

        private System.Windows.Forms.TextBox fidTextBox;

        private System.Windows.Forms.Label FidLabel;

        private System.Windows.Forms.ComboBox tipFructeComboBox;
        private System.Windows.Forms.DataGridView fructeGridView;

        #endregion
    }
}